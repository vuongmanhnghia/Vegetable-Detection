import { Box, Button, Center, Container, Stack } from "@chakra-ui/react";
import React, { useRef, useEffect, useState } from "react";
import Webcam from "react-webcam";

const SERVER_URL = "ws://localhost:8000/ws";

const RealtimeDetection = ({ color }) => {
	const webcamRef = useRef(null);
	const [socket, setSocket] = useState(null);
	const [resultImage, setResultImage] = useState(null);
	const [isRealtime, setIsRealtime] = useState(false);
	const [reconnectAttempts, setReconnectAttempts] = useState(0);

	const connectWebSocket = () => {
		const ws = new WebSocket(SERVER_URL);

		ws.onopen = () => {
			console.log("Connected to WebSocket server");
			setReconnectAttempts(0);
		};

		ws.onerror = (error) => console.error("WebSocket error:", error);

		ws.onmessage = (event) => {
			const data = JSON.parse(event.data);
			if (data.image) {
				setResultImage(`data:image/jpeg;base64,${data.image}`);
			}
		};

		ws.onclose = () => {
			console.warn("WebSocket closed, attempting to reconnect...");
			if (reconnectAttempts < 5) {
				// Giới hạn số lần reconnect
				setTimeout(() => {
					setReconnectAttempts(reconnectAttempts + 1);
					setSocket(connectWebSocket());
				}, 3000);
			}
		};

		return ws;
	};

	useEffect(() => {
		setSocket(connectWebSocket());
		return () => socket?.close();
	}, []);

	const captureFrame = () => {
		if (!isRealtime) {
			return;
		}

		if (webcamRef.current && socket?.readyState === WebSocket.OPEN) {
			const imageSrc = webcamRef.current.getScreenshot();
			if (imageSrc) {
				const img = new Image();
				img.src = imageSrc;
				img.onload = () => {
					// Tạo canvas
					const canvas = document.createElement("canvas");
					const ctx = canvas.getContext("2d");

					// Đặt kích thước canvas
					canvas.width = img.width;
					canvas.height = img.height;

					// Lật ảnh ngang (horizontal flip)
					ctx.translate(canvas.width, 0);
					ctx.scale(-1, 1);

					// Vẽ ảnh lên canvas
					ctx.drawImage(img, 0, 0, img.width, img.height);

					// Chuyển ảnh về base64
					const flippedImageSrc = canvas.toDataURL("image/png");
					const base64Image = flippedImageSrc.split(",")[1]; // Bỏ phần header base64

					// Gửi ảnh lật qua socket
					socket.send(base64Image);
				};
			}
		}
	};

	useEffect(() => {
		const interval = setInterval(captureFrame, 200);
		return () => clearInterval(interval);
	}, [isRealtime, socket]);

	return (
		<Container maxW={"3xl"}>
			<Stack as={Box} textAlign={"center"} spacing={8} pb={20}>
				<Center>
					<Button
						colorScheme={color}
						onClick={() => setIsRealtime(!isRealtime)}>
						Camera {isRealtime ? "Off" : "On"}
					</Button>
				</Center>
				{isRealtime && (
					<>
						<Webcam
							style={{ transform: "scaleX(-1)" }}
							ref={webcamRef}
							screenshotFormat="image/jpeg"
						/>
						<h2>Processed Image:</h2>
						{resultImage && (
							<img
								// style={{ transform: "scaleX(-1)" }}
								src={resultImage}
								alt="Processed"
							/>
						)}
					</>
				)}
			</Stack>
		</Container>
	);
};

export default RealtimeDetection;

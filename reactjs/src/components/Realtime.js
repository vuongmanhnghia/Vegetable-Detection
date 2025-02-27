import { Box, Button, Center, Container, Stack } from "@chakra-ui/react";
import React, { useRef, useEffect, useState } from "react";
import Webcam from "react-webcam";

const SERVER_URL = "ws://localhost:8000/ws";

const RealtimeDetection = ({ color }) => {
	const webcamRef = useRef(null);
	const [socket, setSocket] = useState(null);
	const [resultImage, setResultImage] = useState(null);
	const [isRealtime, setIsRealtime] = useState(false);

	useEffect(() => {
		const ws = new WebSocket(SERVER_URL);
		ws.onopen = () => console.log("Connected to server");
		ws.onmessage = (event) => {
			const data = JSON.parse(event.data);
			if (data.image) {
				setResultImage(`data:image/jpeg;base64,${data.image}`);
			}
		};
		setSocket(ws);
		return () => ws.close();
	}, []);

	const captureFrame = () => {
		if (!isRealtime) {
			return;
		} else {
			if (webcamRef.current && socket?.readyState === WebSocket.OPEN) {
				const imageSrc = webcamRef.current.getScreenshot();
				if (imageSrc) {
					const base64Image = imageSrc.split(",")[1]; // Bỏ phần header của base64
					socket.send(base64Image);
				}
			}
		}
	};

	useEffect(() => {
		const interval = setInterval(captureFrame, 1000 / 5);
		return () => clearInterval(interval);
	}, [socket]);

	return (
		<Container maxW={"3xl"} id="detectionTool">
			<Stack
				as={Box}
				textAlign={"center"}
				spacing={{ base: 8, md: 14 }}
				pb={{ base: 20, md: 36 }}>
				<Stack px={4} spacing={4}>
					<Center px={4}>
						<Button
							colorScheme={color}
							bg={`${color}.400`}
							rounded={"full"}
							px={6}
							_hover={{
								bg: `${color}.500`,
							}}
							onClick={() => setIsRealtime(!isRealtime)}>
							Camere {isRealtime ? "Off" : "On"}
						</Button>
					</Center>
				</Stack>
				{isRealtime && (
					<>
						<Webcam
							ref={webcamRef}
							screenshotFormat="image/jpeg"
							className="border rounded-lg"
						/>
						<h2 className="mt-4">Processed Image:</h2>
						{resultImage && (
							<img
								src={resultImage}
								alt="Processed Result"
								className="border rounded-lg mt-2"
							/>
						)}
					</>
				)}
			</Stack>
		</Container>
	);
};

export default RealtimeDetection;

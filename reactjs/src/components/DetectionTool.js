import {
	Divider,
	Stack,
	Text,
	Container,
	Box,
	HStack,
	Image,
	Button,
	Center,
} from "@chakra-ui/react";

import { useState, useEffect } from "react";
import { detectImage } from "../api";

export default function DetectionTool({ color }) {
	const [imageSrc, setImageSrc] = useState(null);
	const [selectedImage, setSelectedImage] = useState(null);

	const handleImageChange = (event) => {
		const file = event.target.files[0];
		if (file) {
			setSelectedImage(file);
			setImageSrc(URL.createObjectURL(file));
		}
	};

	const handleSubmit = async (event) => {
		event.preventDefault();

		const response = await detectImage(selectedImage);
		setImageSrc(response); // Cập nhật trạng thái với URL ảnh
	};

	return (
		<>
			<Container maxW={"3xl"} id="detectionTool">
				<Stack
					as={Box}
					textAlign={"center"}
					spacing={{ base: 8, md: 14 }}
					pb={{ base: 20, md: 36 }}>
					<Stack align="center" direction="row" px={4}>
						<HStack mx={4}>
							<Text color={`${color}.400`} fontWeight={800}>
								02
							</Text>
							<Text fontWeight={800}>Detection</Text>
						</HStack>
						<Divider orientation="horizontal" />
					</Stack>
					<Center px={4}></Center>
					<Stack px={4} spacing={4}>
						<Center px={4}>
							<div
								// onSubmit={handleSubmit}
								style={{
									display: "flex",
									flexDirection: "column",
									alignItems: "center",
									gap: "1rem",
								}}>
								<input
									style={{ display: "flex", flexDirection: "column" }}
									type="file"
									accept="image/*"
									onChange={handleImageChange}
								/>
								{/* <button type="submit">Upload</button> */}
								<Button
									colorScheme={color}
									bg={`${color}.400`}
									rounded={"full"}
									px={6}
									_hover={{
										bg: `${color}.500`,
									}}
									onClick={handleSubmit}>
									Detect
								</Button>
							</div>
						</Center>
					</Stack>
					<Stack px={4} spacing={4}>
						<Center px={4}>
							{imageSrc && (
								<Image
									border="1px solid red"
									rounded="md"
									h="100%"
									w="100%"
									fit="contain"
									src={imageSrc}
								/>
							)}
						</Center>
					</Stack>
				</Stack>
			</Container>
		</>
	);
}

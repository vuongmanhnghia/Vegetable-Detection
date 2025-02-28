import {
	Divider,
	Stack,
	Text,
	Container,
	Box,
	HStack,
	Heading,
	Center,
} from "@chakra-ui/react";
import { FaLinkedin, FaGithub, FaEnvelope } from "react-icons/fa";

export default function Contact({ color }) {
	const linkedin = () => {};
	const github = () => {
		window.open(
			"https://github.com/vuongmanhnghia/Vegetable-Detection.git",
			"_blank"
		); // Mở link trong tab mới
	};
	const email = () => {};
	return (
		<>
			<Container maxW={"3xl"} id="contact">
				<Stack
					as={Box}
					textAlign={"center"}
					spacing={{ base: 8, md: 14 }}
					pb={{ base: 20, md: 36 }}>
					<Stack align="center" direction="row" p={4}>
						<HStack mx={4}>
							<Text color={`${color}.400`} fontWeight={800}>
								04
							</Text>
							<Text fontWeight={800}>Contact</Text>
						</HStack>
						<Divider orientation="horizontal" />
					</Stack>
					<Stack
						spacing={4}
						as={Container}
						maxW={"3xl"}
						textAlign={"center"}>
						<Heading fontSize={"3xl"} color={`gray.500`} fontWeight={700}>
							Contact me if you need help!
						</Heading>
						<Text color={"gray.600"} fontSize={"xl"} px={4}></Text>
						<Text
							color={`${color}.500`}
							fontWeight={600}
							fontSize={"lg"}
							px={4}></Text>
						<Center>
							<HStack pt={4} spacing={4}>
								<FaGithub onClick={github} size={50} />
							</HStack>
						</Center>
					</Stack>
				</Stack>
			</Container>
		</>
	);
}

import { Divider, Stack, Text, Container, Box, HStack } from "@chakra-ui/react";

export default function About({ color }) {
	return (
		<>
			<Container maxW={"3xl"} id="about">
				<Stack
					as={Box}
					textAlign={"center"}
					spacing={{ base: 8, md: 14 }}
					pb={{ base: 20, md: 36 }}>
					<Stack align="center" direction="row" px={4}>
						<HStack mx={4}>
							<Text color={`${color}.400`} fontWeight={800}>
								01
							</Text>
							<Text fontWeight={800}>About</Text>
						</HStack>
						<Divider orientation="horizontal" />
					</Stack>
					<Text color={"gray.600"} fontSize={"xl"} px={4}>
						Our <b>Vegetable Detection Project</b> utilizes advanced
						computer vision and machine learning techniques to accurately
						identify various types of vegetables. This system is designed
						to assist in agricultural automation, food quality control,
						and smart retail solutions. By leveraging deep learning
						models, our solution can recognize vegetables in real time,
						improving efficiency in sorting, classification, and inventory
						management. The project aims to enhance productivity, reduce
						food waste, and support sustainability efforts in the food
						industry.
					</Text>
				</Stack>
			</Container>
		</>
	);
}

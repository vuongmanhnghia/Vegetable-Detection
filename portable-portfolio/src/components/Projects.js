import {
	Divider,
	Stack,
	Text,
	Container,
	Box,
	HStack,
	Button,
	ButtonGroup,
	Card,
	CardBody,
	Image,
	Heading,
	SimpleGrid,
	Badge,
	Link,
	Center,
} from "@chakra-ui/react";
import { Fade } from "react-reveal";
import { useState } from "react";
import ProjectsArray from "./ProjectsArray";
import OtherProjectsArray from "./OtherProjectsArray";

export default function Projects({ color }) {
	const projects = ProjectsArray();
	const others = OtherProjectsArray();

	const [selected, setSelected] = useState("All");

	const handleSelected = (value) => {
		setSelected(value);
	};

	return (
		<>
			<Container maxW={"3xl"} id="history">
				<Stack
					as={Box}
					textAlign={"center"}
					spacing={{ base: 8, md: 14 }}
					pb={{ base: 20, md: 36 }}>
					<Stack align="center" direction="row" p={4}>
						<HStack mx={4}>
							<Text color={`${color}.400`} fontWeight={800}>
								03
							</Text>
							<Text fontWeight={800}>Projects</Text>
						</HStack>
						<Divider orientation="horizontal" />
					</Stack>
					<Stack px={4} spacing={4}>
						{projects.map((project) => (
							<Fade bottom>
								<Card
									key={project.name}
									direction={{
										base: "column",
									}}
									overflow="hidden">
									<Image objectFit="cover" src={project.image} />

									<Stack>
										<CardBody align="left">
											<Heading size="md">{project.name}</Heading>

											<Text py={2}>{project.description}</Text>

											<HStack py={2}>
												{project.buttons.map((button) => (
													<a key={button.text} href={button.href}>
														<Button color={`${color}.400`}>
															{button.text}
														</Button>
													</a>
												))}
											</HStack>
											<HStack pt={4} spacing={2}>
												{project.badges.map((badge) => (
													<Badge
														key={badge.text}
														colorScheme={badge.colorScheme}>
														{badge.text}
													</Badge>
												))}
											</HStack>
										</CardBody>
									</Stack>
								</Card>
							</Fade>
						))}
					</Stack>
				</Stack>
			</Container>
		</>
	);
}

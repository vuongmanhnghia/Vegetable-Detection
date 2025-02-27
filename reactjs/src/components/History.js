import {
	Divider,
	Stack,
	Text,
	Container,
	Box,
	HStack,
	Image,
	CardBody,
	Card,
} from "@chakra-ui/react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setHistories } from "../store";
import { API_APP_URL } from "../configs/constants";
import { getHistory } from "../api";
import { Button } from "react-bootstrap";

export default function Projects({ color }) {
	const dispatch = useDispatch();
	const { histories } = useSelector((state) => state.auth);

	useEffect(() => {
		fetchHistories();
	}, []);

	const fetchHistories = async () => {
		const histories = await getHistory();
		dispatch(setHistories(histories));
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
							<Text fontWeight={800}>History</Text>
						</HStack>
						<Divider orientation="horizontal" />
					</Stack>
					<Stack px={4} spacing={4}>
						{histories?.map((history, index) => (
							<Card
								margin={"0 5rem"}
								style={{ padding: "0.5rem" }}
								direction={{ base: "column", sm: "row" }}
								overflow="hidden"
								variant="outline">
								<Image
									cursor={"pointer"}
									width={{ base: "100%" }}
									objectFit="cover"
									height={{ base: "200px" }}
									src={`${API_APP_URL}${history.image_url}`}
									alt="Caffe Latte"
									onClick={() =>
										window.open(`${API_APP_URL}${history.image_url}`)
									}
								/>
							</Card>
						))}
					</Stack>
				</Stack>
			</Container>
		</>
	);
}

import {
	Divider,
	Stack,
	Text,
	Container,
	Box,
	HStack,
	Image,
} from "@chakra-ui/react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setHistories } from "../store";
import { API_APP_URL } from "../configs/constants";
import { getHistory } from "../api";

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
							<Image
								index={index}
								border="1px solid red"
								rounded="md"
								h="200px"
								w="100%"
								fit="contain"
								src={`${API_APP_URL}${history.image_url}`}
							/>
						))}
					</Stack>
				</Stack>
			</Container>
		</>
	);
}

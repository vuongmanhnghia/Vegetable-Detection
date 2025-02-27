import React, { useEffect } from "react";
import "./App.css";
import Nav from "./components/NavBar";
import Header from "./components/Header";
import About from "./components/About";
import DetectionTool from "./components/DetectionTool";
import History from "./components/History";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
import { useDispatch } from "react-redux";
import { getHistory, getMe } from "./api";
import { setAuthUser } from "./store";
import RealtimeDetection from "./components/Realtime";

function App() {
	const dispatch = useDispatch();

	useEffect(() => {
		handleGetMe();
	}, []);

	const handleGetMe = async () => {
		const user = await getMe();
		if (user) {
			dispatch(setAuthUser(user));
			await getHistory();
		}
	};

	const color = "teal";

	return (
		<>
			<Nav color={color} />
			<Header color={color} />
			<About color={color} />
			<DetectionTool color={color} />
			<RealtimeDetection color={color} />
			<History color={color} />
			<Contact color={color} />
			<Footer />
		</>
	);
}

export default App;

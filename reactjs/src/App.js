import React, { useEffect } from "react";
import "./App.css";
import Nav from "./components/NavBar";
import Header from "./components/Header";
import About from "./components/About";
import DetectionTool from "./components/DetectionTool";
import Projects from "./components/History";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
import { useDispatch } from "react-redux";
import { getMe } from "./api";
import { setAuthUser } from "./store";

function App() {
	const dispatch = useDispatch();
	useEffect(() => {
		// handleGetMe();
	}, []);

	const handleGetMe = async () => {
		const user = await getMe();
		dispatch(setAuthUser(user));
	};

	const color = "teal";

	return (
		<>
			<Nav color={color} />
			<Header color={color} />
			<DetectionTool color={color} />
			<Projects color={color} />
			<About color={color} />
			<Contact color={color} />
			<Footer />
		</>
	);
}

export default App;

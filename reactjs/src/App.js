import React, { useEffect, useCallback } from "react";
import "./App.css";
import Nav from "./components/NavBar";
import Header from "./components/Header";

import DetectionTool from "./components/DetectionTool";
import History from "./components/History";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
import { useDispatch } from "react-redux";
import { getMe } from "./api";
import { setAuthUser } from "./store";
import Particles from "react-tsparticles";
import particlesConfig from "./particlesConfig";

function App() {
  const dispatch = useDispatch();
  const handleGetMe = useCallback(async () => {
    const user = await getMe();
    dispatch(setAuthUser(user));
  }, [dispatch]);

  useEffect(() => {
    handleGetMe();
  }, [handleGetMe]);

  const color = "teal";

  return (
    <div className="App">
      <Particles params={particlesConfig} />
      <div className="content">
        <Nav color={color} />
        <Header color={color} />
        <DetectionTool color={color} />
        <History color={color} />
        <Contact color={color} />
        <Footer />
      </div>
    </div>
  );
}

export default App;
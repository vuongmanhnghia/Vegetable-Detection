import React from "react";
import ReactDOM from "react-dom/client";
import { ColorModeScript } from "@chakra-ui/react";
import "./index.css";
import App from "./App";
import theme from "./theme";
import reportWebVitals from "./reportWebVitals";
import { ChakraProvider } from "@chakra-ui/react";
import { GoogleOAuthProvider } from "@react-oauth/google";
import { GG_CLIENT_ID } from "./configs/constants";
import { Provider } from "react-redux";
import store from "./store";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
	<ChakraProvider theme={theme}>
		<React.StrictMode>
			<ColorModeScript initialColorMode={theme.config.initialColorMode} />
			<GoogleOAuthProvider clientId={GG_CLIENT_ID}>
				<Provider store={store}>
					<App />
				</Provider>
			</GoogleOAuthProvider>
		</React.StrictMode>
	</ChakraProvider>
);

reportWebVitals();

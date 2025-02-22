import axios from "axios";
import { API_APP_URL } from "../configs/constants";

export const loginGoogle = async (googleToken) => {
	try {
		const response = await axios.post(
			`${API_APP_URL}/auth/google?token=${googleToken}`,
			{
				headers: {
					"Content-Type": "application/json",
				},
			}
		);
		return response;
	} catch (error) {
		return error;
	}
};

export const detectImage = async (image) => {
	const formData = new FormData();
	formData.append("file", image);

	try {
		const response = await axios.post(
			"http://localhost:8000/users/predict/",
			formData
		);
		return `${API_APP_URL}${response.data.data}`;
	} catch (error) {
		return error;
	}
};

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
		localStorage.setItem("user_id", response.data.data._id);
		return response;
	} catch (error) {
		return error;
	}
};

export const getMe = async () => {
	try {
		const user_id = localStorage.getItem("user_id");
		const response = await axios.get(
			`${API_APP_URL}/auth/me?user_id=${user_id}`
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
			`${API_APP_URL}/users/predict/`,
			formData
		);
		return response.data.data;
	} catch (error) {
		return error;
	}
};

export const saveImage = async (image_url) => {
	try {
		const user_id = localStorage.getItem("user_id");
		const response = await axios.post(
			`${API_APP_URL}/users/save?image_url=${image_url}`,
			{},
			{
				headers: {
					user_id: user_id,
					"Content-Type": "application/json",
				},
			}
		);

		return response;
	} catch (error) {
		return error;
	}
};

export const getHistory = async () => {
	try {
		const user_id = localStorage.getItem("user_id");
		const response = await axios.get(`${API_APP_URL}/users/history`, {
			headers: {
				user_id: user_id,
				"Content-Type": "application/json",
			},
		});
		return response;
	} catch (error) {
		return error;
	}
};

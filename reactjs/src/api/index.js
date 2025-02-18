import axios from "axios";

export const loginGoogle = async (token) => {
	try {
		const response = await axios.post(
			"http://localhost:8000/auth/google/",
			{ token: token }, // Đảm bảo token được gửi dưới dạng JSON
			{
				headers: {
					"Content-Type": "application/json", // Đặt header Content-Type là application/json
				},
			}
		);
		return response;
	} catch (error) {
		return error;
	}
};

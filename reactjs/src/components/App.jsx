import React, { useState } from "react";

function App() {
	const [selectedImage, setSelectedImage] = useState(null);
	const [imageSrc, setImageSrc] = useState(null);

	// Xử lý việc chọn ảnh từ người dùng
	const handleImageChange = (event) => {
		const file = event.target.files[0];
		if (file) {
			setSelectedImage(file);
		}
	};

	// Gửi ảnh lên backend (FastAPI)
	const handleSubmit = async (event) => {
		event.preventDefault();

		// Tạo FormData để gửi file
		const formData = new FormData();
		formData.append("file", selectedImage);

		try {
			// Gửi yêu cầu POST đến backend để upload ảnh
			const response = await fetch("http://127.0.0.1:8000/users/predict", {
				method: "POST",
				body: formData,
			});

			// Kiểm tra nếu yêu cầu thành công
			if (response.ok) {
				// Nhận ảnh và tạo URL để hiển thị
				const imageBlob = await response.blob();
				const imageUrl = URL.createObjectURL(imageBlob);
				setImageSrc(imageUrl); // Cập nhật trạng thái với URL ảnh
			} else {
				console.error("Error uploading image:", response.statusText);
			}
		} catch (error) {
			console.error("Error:", error);
		}
	};

	return (
		<div className="App">
			<h1>Upload an Image</h1>
			<form onSubmit={handleSubmit}>
				<input type="file" accept="image/*" onChange={handleImageChange} />
				<button type="submit">Upload</button>
			</form>

			{imageSrc && (
				<div>
					<h2>Uploaded Image:</h2>
					<img
						src={imageSrc}
						alt="Uploaded"
						style={{ maxWidth: "100%", maxHeight: "400px" }}
					/>
				</div>
			)}
		</div>
	);
}

export default App;

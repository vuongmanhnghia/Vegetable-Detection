import { configureStore, createSlice } from "@reduxjs/toolkit";

// Bước 1: Tạo slice (bao gồm reducer và action)
const authSlice = createSlice({
	name: "counter",
	initialState: {
		authUser: {},
	},
	reducers: {
		setAuthUser(state, action) {
			state.authUser = action.payload.data.data;
		},
	},
});

// Bước 2: Tạo store với reducer từ slice
const store = configureStore({
	reducer: {
		auth: authSlice.reducer,
	},
});

export const { increment, decrement, setAuthUser } = authSlice.actions;
export default store;

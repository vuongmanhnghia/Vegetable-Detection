import { configureStore, createSlice } from "@reduxjs/toolkit";

// Bước 1: Tạo slice (bao gồm reducer và action)
const authSlice = createSlice({
	name: "counter",
	initialState: {
		authUser: {},
		histories: [],
	},
	reducers: {
		setAuthUser(state, action) {
			state.authUser = action.payload.data.data;
		},
		setHistories(state, action) {
			state.histories = action.payload.data.data;
		},
	},
});

const store = configureStore({
	reducer: {
		auth: authSlice.reducer,
	},
});

export const { increment, decrement, setAuthUser, setHistories } =
	authSlice.actions;
export default store;

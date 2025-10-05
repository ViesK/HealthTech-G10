import { createSlice, type PayloadAction } from "@reduxjs/toolkit";

type State = { token?: string };
const initial: State = {};
const slice = createSlice({
    name: "auth",
    initialState: initial,
    reducers: {
        setToken: (s, a: PayloadAction<string|undefined>) => { s.token = a.payload; },
        logout: (s) => { s.token = undefined; }
    }
});
export const { setToken, logout } = slice.actions;
export default slice.reducer;

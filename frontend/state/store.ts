'use client'
import { configureStore } from "@reduxjs/toolkit";
import listReducer from "./listStore/listSlice"
import groupsReducer from "./groupStore/groupSlice"
import camerasReducer from "./complexStore/complexSlice"
import { ListType } from "@/lib/types";

export const store = configureStore({
    reducer: {
        list: listReducer,
        groups: groupsReducer,
        cameras: camerasReducer
    }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
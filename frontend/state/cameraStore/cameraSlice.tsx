'use client'
import AddCamera from "@/components/modals/AddCamera"
import {  } from "@/http/someAPI"
import { CamerasData, GroupsData, ListType } from "@/lib/types"
import { createSlice } from "@reduxjs/toolkit"

const initialState: CamerasData[] = []

const cameraSlice = createSlice({
    name:'cameras', 
    initialState,
    reducers: {
        setCameras: (state, action) => {
            return state =  [...state, action.payload]
        },
        removeCamera: (state, action) => {
            state = state.splice(state.findIndex(e => e.uuid === action.payload))
        },
    }
})

export const {setCameras, removeCamera} = cameraSlice.actions

export default cameraSlice.reducer
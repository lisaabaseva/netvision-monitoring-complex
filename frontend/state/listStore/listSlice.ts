'use client'
import AddCamera from "@/components/modals/AddComplex"
import {  } from "@/http/someAPI"
import { ListType } from "@/lib/types"
import { createSlice } from "@reduxjs/toolkit"

const initialState: ListType[] = []

const listSlice = createSlice({
    name:'list', 
    initialState,
    reducers: {
        setList: (state, action: {payload: ListType[]}) => {
           // console.log('action', action)
            //console.log('action134234', action.payload)
            return state = action.payload
           // state.map(s => console.log('s', s))
        },
        addList: (state, action: {payload: ListType}) => {
           // console.log('action', action)
            return state =  [...state, action.payload]
        },
        removeList: (state, action:{payload: string}) => {
            state = state.splice(state.findIndex(e => e.listId === action.payload))
        },
        addCamera: (state, action) => {
            return state = [...state, {...action.payload.list, content: [...action.payload.camera, ]}]
        } 
    }
})

export const {setList, addList ,removeList} = listSlice.actions

export default listSlice.reducer
'use client'
import AddCamera from "@/components/modals/AddComplex"
import {  } from "@/http/someAPI"
import { ComplexData, GroupsData, ListType } from "@/lib/types"
import { createSlice } from "@reduxjs/toolkit"

const initialState: ComplexData[] = []

const complexSlice = createSlice({
    name:'cameras', 
    initialState,
    reducers: {
        setComplex: (state, action) => {
            return state =  [...state, action.payload]
        },
        removeComplex: (state, action) => {
            state = state.splice(state.findIndex(e => e.uuid === action.payload))
        },
    }
})

export const {setComplex, removeComplex} = complexSlice.actions

export default complexSlice.reducer
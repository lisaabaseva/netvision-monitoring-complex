'use client'
import AddCamera from "@/components/modals/AddComplex"
import { GroupsData, ListType } from "@/lib/types"
import { createSlice } from "@reduxjs/toolkit"

const initialState: GroupsData[] = []

const groupSlice = createSlice({
    name:'groups', 
    initialState,
    reducers: {
        setGroups: (state, action) => {
            return state =  [...state, action.payload]
        },
        removeGroup: (state, action) => {
            state = state.splice(state.findIndex(e => e.uuid === action.payload))
        },
    }
})

export const {setGroups, removeGroup} = groupSlice.actions

export default groupSlice.reducer
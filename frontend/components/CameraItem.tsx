'use client'
import { deleteGroup } from "@/http/someAPI"
import { ComplexData, Complex, CamerasData } from "@/lib/types"
import { removeComplex } from "@/state/complexStore/complexSlice"
import { useDispatch } from "react-redux"
import CameraInfo from "./modals/ComplexInfo"
import { useEffect, useState } from "react"

const CameraItem = (props: {camera: CamerasData}) => {
    const dispatch = useDispatch()
    let hui = {
        description: 'yavahue',
        url: 'pohui://666:666',
        id: 'kakoi id?',
        active: true,
        status: 1
     }
    let vkl = {text: 'Off', color: 'bg-red-500'}
         if (props.camera.active) {
            vkl = {text: 'On', color: 'bg-green-500'}
          }
    let st = {text: 'OK', color: 'bg-green-500'}
    if (props.camera.status == 0) {
       st = {text: 'Failure', color: 'bg-red-500'}
    }
    return (
        <tr className="w-full cursor-pointer">
            <td className="w-1/3 py-2">{props.camera.description}</td>
            <td className="w-1/4">{props.camera.url}</td>
            <td className="w-1/12 bg-green-500/0">{props.camera.id}</td>
            <td>
            <div className={`w-fit h-fit ${vkl.color} rounded-xl mx-auto px-3 py-1 border-3 border-netvision-gradient-end`}>{vkl.text}</div>
            </td>
            <td className={`w-1/5 bg-red-500/0`}>
                <div className={`w-fit h-fit ${st.color} rounded-xl mx-auto px-3 py-1 border-3 border-netvision-gradient-end`}>{st.text}</div>
            </td>
        </tr>
    )
}

export default CameraItem


/**
 *         <tr className="w-full cursor-pointer">
            <td className="w-1/3 py-2">{props.camera.description}</td>
            <td className="w-1/4">{props.camera.url}</td>
            <td className="w-1/12 bg-green-500/0">{props.camera.id}</td>
            <td>{props.camera.active}</td>
            <td className={`w-1/5 bg-red-500/0`}>
                <div className={`w-fit h-fit ${st.color} rounded-xl mx-auto px-3 py-1 border-3 border-netvision-gradient-end`}>{st.text}</div>
            </td>
        </tr>

        <div className={`w-fit h-fit ${vkl.color} rounded-xl mx-auto px-3 py-1 border-3 border-netvision-gradient-end`}>{vkl.text}</div>
 */
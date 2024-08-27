'use client'
import { deleteComplex, deleteGroup } from "@/http/someAPI"
import { ComplexData, Complex } from "@/lib/types"
import { removeComplex } from "@/state/complexStore/complexSlice"
import { useDispatch } from "react-redux"
import { useState } from "react"
import ComplexInfo from "./modals/ComplexInfo"

const ComplexItem = (props: {complex: Complex}) => {
    const dispatch = useDispatch()
    let st = {text: 'OK', color: 'bg-green-500'}
    if (props.complex.status?.int == 0) {
       st = {text: 'Failure', color: 'bg-red-500'}
    }

    const [cameraInfoModal, setCameraInfoModal] = useState(false)

    const deleteHandler = async () => {
        deleteComplex(props.complex.uuid)
        dispatch(removeComplex(props.complex.uuid))
        //location.reload()
        //dispatch(removeList(props.item.listId))
      }

    return (
        <tr className="w-full cursor-pointer" onClick={() => {setCameraInfoModal(true)}}>
            <td className="w-1/3 py-2">{props.complex.name}</td>
            <td className="w-1/4">{props.complex.ip}</td>
            <td className="w-1/12 bg-green-500/0">{props.complex.port}</td>
            <td className={`w-1/5 bg-red-500/0`}>
                <div className={`w-fit h-fit ${st.color} rounded-xl mx-auto px-3 py-1 border-3 border-netvision-gradient-end`}>{st.text}</div>
            </td>
            <td className="min-w-fit flex" onClick={e => e.stopPropagation()}>
                <button className="w-1/3 inline mr-1">
                    <img src="/icons/pen-light.svg" width={30} alt="trash" className="inline"/>
                </button>
                <button onClick={deleteHandler} className="inline mr-auto">
                <img src="/icons/trash-light.svg" width={30} alt="trash" className="inline"/>
                </button>
                <div onClick={e => e.stopPropagation()} className="bg-orange-500 ">
                <ComplexInfo show={cameraInfoModal} onHide={() => {setCameraInfoModal(false)}} uuid={props.complex.uuid} cameras={props.complex.cameras}/>
                </div>
            </td>            
        </tr>
    )
}

export default ComplexItem

//<td className="w-4/12">{props.complex.uuid}</td>
'use client'
import { ListType } from "@/lib/types"
import { useEffect, useState } from "react"
import ComplexItem from "./ComplexItem"
import { useDispatch, useSelector } from "react-redux"
import { RootState } from "@/state/store"
import { removeList } from "@/state/listStore/listSlice"
import AddCamera from "./modals/AddComplex"
import { deleteGroup } from "@/http/someAPI"
import AddCameraToList from "./modals/AddComplexToList"
import CameraInfo from "./modals/ComplexInfo"


const ListItem = (props: {item:ListType}) => {
  const [AddCameraModal, setAddCameraModal] = useState(false)
  const [editListModal, setEditListModal] = useState(false)
  const [isActive, setIsActve] = useState(false)
  const list: ListType[] = Array.from(useSelector((state: RootState) => state.list))
  const dispatch = useDispatch()
  const clickHandler = () => {
    setIsActve(!isActive)
  }
  const deleteHandler = async () => {
    deleteGroup(props.item.listId).then(() => location.reload())
    //location.reload()
    //dispatch(removeList(props.item.listId))
  }

  return (
    <div key={props.item.listId} className="mb-3">
    <div className="h-14 w-full bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end rounded-xl text-white px-10 flex">
      <button onClick={clickHandler} className="h-full w-2/3 min-w-fit text-left inline">
        {props.item.name}
      </button>
      <div className="w-1/6 inline-flex items-center mx-auto min-w-fit">
        Статус:
        <div className={`ml-1 w-fit ${props.item.status.color} p-1 rounded-xl px-3 border-3 border-netvision-gradient-start`}>
          {props.item.status.text}
        </div>
      </div>
      <div className="w-1/6 inline-flex min-w-fit">
        <button className="w-1/3 inline ml-auto">
          <img src="/icons/pen-light.svg" width={40} alt="trash" className="inline"/>
        </button>
        <button onClick={deleteHandler} className="ml-2 inline">
          <img src="/icons/trash-light.svg" width={40} alt="trash" className="inline"/>
        </button>
      </div>
    </div>
    
    {isActive && <div className="bg-gradient-to-b from-netvision-gradient2-start to-netvision-gradient2-end mt-2 rounded-xl py-2">
      <table className="w-full text-center table-fixed">
          {(props.item.content?.length) ?
          <tbody>
            {props.item.content.map((i) => 
              <ComplexItem key={i.ip + ':' + i.port} complex={i}/>
            )}
          </tbody>
          :<tbody>
              <tr>
                <td className="w-full">Список пуст</td>
              </tr>
           </tbody>
          }
      </table>
      <button onClick={() => {setAddCameraModal(true)}} className="mt-2 block w-1/5 min-w-fit mx-auto bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end p-2 rounded-xl px-5">
        <img src="/icons/plus-light.svg" alt="list" width={30} className="inline"/>
        <p className="inline ml-2">Добавить комплекс</p>
      </button>
    </div>}
    <AddCameraToList show={AddCameraModal} onHide={() => {setAddCameraModal(false)}} newList={props.item}/>
  </div>
  )
}

export default ListItem
// <AddCamera show={AddCameraModal} onHide={() => {setAddCameraModal(false)}} newList={props.item}/>
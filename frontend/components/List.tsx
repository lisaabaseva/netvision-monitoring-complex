'use client'
import { useEffect, useState } from "react"
import ComplexItem from "./ComplexItem"
import { ComplexData, Complex, GroupsData, ListType } from "@/lib/types"
import { getCameras, getGroups } from "@/http/someAPI"
import ListItem from "./ListItem"
import { useDispatch, useSelector } from "react-redux"
import { RootState } from "@/state/store"
import { createSelector } from "@reduxjs/toolkit"
import { setGroups } from "@/state/groupStore/groupSlice"
import { removeComplex } from "@/state/complexStore/complexSlice"
import { setList } from "@/state/listStore/listSlice"
import { group } from "console"
import { useFetchAll } from "@/hooks/useFetchAll"
import { setInterval } from "timers"


const List = () => {
  //const [list, setList] = useState<ListItem[]>([{listId: 0, name : 'test', content: [{uuid: 0, name: 'example', ip: '123.45.67.89', port: 777, status: 'ok'} ]}])
  //const [list, setList] = useState<ListType[]>([{listId: 0, name : 'test', status: 1, content: [{uuid: 'example', ip: '123.45.67.89', port: 777, login: '', password: '', status: 1} ]}, {listId: 1, name : 'test1', status: 1, content: [{uuid: 'example1', ip: '123.45.67.90', port: 7771, login: '', password: '', status: 1} ]}])
  
  //const selectA = (state: RootState) => state.list
  //const selectList = createSelector([selectA], (list) => {return(Array.from(list.values()))})
  /**useEffect(() => {
    let lists: ListType[] =  selectList(state)
  }, [])*/
  const dispatch = useDispatch()
  const groups: GroupsData[] = Array.from(useSelector((state: RootState) => state.groups))
  const cameras: ComplexData[] = Array.from(useSelector( (state: RootState) => state.cameras))
/*  const createList = () => {
    
    groups.map( (group: GroupsData) => {
        //let cameraList = cameras.filter((camera:CamerasData) => camera.group_uuid === group.uuid)
        let cameraList:CamerasData[] = []
        let newList:ListType = {
            listId: group.uuid,
            name: group.name,
            status: 0,
            content: cameraList
        }
       // dispatch(setList(newList))
        console.log('fg')
    })
}*/

useEffect( () => {
  //getGroups().then(data => data.map((i) => dispatch(setGroups(i))))
  //getCameras().then(data => data.map( (i) => dispatch(setCameras(i))))
  //createList()
  //useFetchAll()
  const getLists = async ( ) => {
    dispatch(setList( await useFetchAll()))
  }
  getLists()
  //setInterval(getLists, 5000) 
  //console.log('alo', groups)
  //console.log('list', cameras)
},[])

const list = Array.from(useSelector((state: RootState) => state.list))

  return (
    <div className="w-5/6 mx-auto mt-7">
      <table className="text-white w-full text-center mb-2">
        <thead>
          <tr className="divide-x-2 table-fixed">
            <th className="w-1/3">Наименование</th>
            <th className="w-1/4">IP</th>
            <th className="w-1/12">Port</th>
            <th className="w-1/5">Статус</th>
            <th className="!border-l-0"></th>
          </tr>
        </thead>
      </table>
      {list?.map((item) => { return(
        <ListItem key={item.listId} item={item}/>
      )})}
    </div>
  )
}


export default List

//<GroupItem key={item.uuid} item={item}/>
//<button className="w-32 bg-white text-black">tyazhelo</button>
//<ListItem key={item.listId} item={item}/>
/**
 * {list?.map((item) => { return(
        <div key={item.listId} >
          <button onClick={clickHandler} className="h-14 w-full bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end p-2 rounded-xl px-5 text-left pl-12 mt-7">
            {item.name}
          </button>
          {isActive &&  <div className="bg-gradient-to-b from-netvision-gradient2-start to-netvision-gradient2-end mt-2 rounded-xl py-3">
              <table className="w-full text-center table-fixed">
                <tbody>{(cameras.map((obj) => { return (
                <ComplexItem key={obj.uuid} complex={obj}/>
              )
  
              }))}</tbody></table>
            
            <button className="mt-2 block w-1/5 mx-auto bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end p-2 rounded-xl px-5">
              Create
            </button>
            </div>}
        </div>
      )})}
 */

/**
 * {isActive &&  <div className="bg-gradient-to-b from-netvision-gradient2-start to-netvision-gradient2-end mt-2 rounded-xl py-3">
            {(item?.content)
              ?<table className="w-full text-center table-fixed">
                <tbody>{(item?.content?.map((obj) => { return (
                <ComplexItem key={obj.uuid} complex={obj}/>
              )
  
              }))}</tbody></table>
              : <div>Nothing</div>
            }
            
            <button className="mt-2 block w-1/5 mx-auto bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end p-2 rounded-xl px-5">
              Create
            </button>
            </div>}
 */
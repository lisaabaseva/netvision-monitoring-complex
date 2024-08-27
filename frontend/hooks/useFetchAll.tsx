'use client'

import { getCameras, getComplexes, getGroups } from "@/http/someAPI"
import { CamerasData, Complex, ComplexData, GroupsData, ListType } from "@/lib/types"
import { setComplex } from "@/state/complexStore/complexSlice"
import { setGroups } from "@/state/groupStore/groupSlice"
import { setList } from "@/state/listStore/listSlice"
import { useState } from "react"
import { useDispatch } from "react-redux"

export const useFetchAll = async () => {
  let fetchedGroups: GroupsData[] = []
  let fetchedComplexes: ComplexData[] = []
  let fetchedCameras: CamerasData[] = []
  let compiledComplexes: Complex[] = []
  let compiledLists: ListType[] = []
  //const dispatch = useDispatch()
  await getGroups().then(data => {data.map((i) => {
    //dispatch(setGroups(i))
    fetchedGroups.push(i)
    //console.log('group', i)
  }) 
 // console.log('newGroup', fetchedGroups)
  })
  await getComplexes().then(data => data.map((i: ComplexData) => {
    fetchedComplexes.push(i)
  }))
  await getCameras().then(data => {data.map((i:CamerasData) => {
    //dispatch(setCameras(i))
    fetchedCameras.push(i)
   // console.log('camera', i)
  })
 // console.log('newCamera', fetchedCameras)
  })


  let complexStatus = {text: 'OK', color: 'bg-green-500', int: 1} 

  const ComplexStatusChecker =(complex: Complex) => {
    let statusCounter = 0
    let cameras = fetchedCameras.filter((camera:CamerasData) => camera.complex_uuid === complex.uuid)   
    cameras.map((camera: CamerasData) => {
      if (camera.status){
      statusCounter += camera?.status 
    }
  })
  if (statusCounter == cameras.length) {
    console.log('green', statusCounter)
    console.log('green', cameras.length)
    complexStatus = {text:'OK', color: 'bg-green-500', int: 1}
   } else if (statusCounter == 0) {
    console.log('red', statusCounter)
    console.log('red', cameras.length)
    complexStatus =  { text: 'Failure', color: 'bg-red-500', int: 0}
   } else {
    console.log('yellow',statusCounter === 1)
    console.log('yellow',statusCounter)
    console.log('yellow', cameras.length) 
    complexStatus =  { text: 'Not OK', color: 'bg-orange-500', int: 0}
   }
  }


  let globalStatus = {text: 'OK', color: 'bg-green-500'}
  const globalStatusChecker =(group: GroupsData) => {
    let statusCounter = 0
    let complexes = fetchedComplexes.filter((complex:Complex) => complex.group_uuid === group.uuid)   
    complexes.map((complex: Complex) => {
      if((complex?.status) && (complex.status.int)) {
        statusCounter += complex?.status?.int
      } 
      
    })
    
    /*switch (statusCounter) {
      case (cameras.length):
        console.log('green', statusCounter)
        console.log('green', cameras.length)
        globalStatus = {text:'OK', color: 'bg-green-500'}
        break
      case 0:
        console.log('red', statusCounter)
        console.log('red', cameras.length)
        globalStatus =  { text: 'Sovsem NOT OK', color: 'bd-red-500' }
        break
      default:
        console.log('yellow',statusCounter === 1)
        console.log('yellow',statusCounter)
        console.log('yellow', cameras.length) 
        globalStatus =  { text: 'Not OK', color: 'bg-yellow-500'}
        break
    }*/
   if (statusCounter == complexes.length) {
    console.log('green', statusCounter)
    console.log('green', complexes.length)
    globalStatus = {text:'OK', color: 'bg-green-500'}
   } else if (statusCounter == 0) {
    console.log('red', statusCounter)
    console.log('red', complexes.length)
    globalStatus =  { text: 'Failure', color: 'bg-red-500' }
   } else {
    console.log('yellow',statusCounter === 1)
    console.log('yellow',statusCounter)
    console.log('yellow', complexes.length) 
    globalStatus =  { text: 'Not OK', color: 'bg-orange-500'}
   }
  }
  
  fetchedComplexes.map((complex) => {
    ComplexStatusChecker(complex)
    compiledComplexes = [...compiledComplexes, {
      name: complex.name,
      uuid: complex.uuid,
      ip: complex.ip,
      port: complex.port,
      group_uuid: complex.group_uuid,
      cameras: fetchedCameras.filter((camera: CamerasData) => camera.complex_uuid === complex.uuid),
      status: complexStatus

    }]
  })

  fetchedGroups.map((group) => {
    globalStatusChecker(group)
    compiledLists =[...compiledLists, {
      listId: group.uuid,
      name: group.name,
      status: globalStatus,
      content: compiledComplexes.filter((complex:ComplexData) => complex.group_uuid === group.uuid)
    }]
    
  })
  //dispatch(setList(newList))
  //console.log('newList', compiledLists)
  return compiledLists
} 
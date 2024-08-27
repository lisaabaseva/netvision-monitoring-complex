import { getCameras, getGroups } from "@/http/someAPI"
import { CamerasData, GroupsData, ListType } from "@/lib/types"
import { setCameras } from "@/state/complexStore/complexSlice"
import { setGroups } from "@/state/groupStore/groupSlice"
import { setList } from "@/state/listStore/listSlice"
import { RootState } from "@/state/store"
import { useDispatch, useSelector } from "react-redux"

/** 
export const createList = () => {
    const dispatch = useDispatch()
    getGroups().then(data => dispatch(setGroups(data)))
    getCameras().then(data => dispatch(setCameras(data)))
    const groups: GroupsData[] = Array.from(useSelector((state: RootState) => state.groups))
    const cameras: CamerasData[] = Array.from(useSelector( (state: RootState) => state.cameras))
    groups.map((group: GroupsData) => {
        let cameraList = cameras.filter((camera:CamerasData) => camera.group_uuid === group.uuid)
        let newList:ListType = {
            listId: group.uuid,
            name: group.name,
            status: 0,
            content: cameraList
        }
        dispatch(setList(newList))
    })
}*/
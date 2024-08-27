import {CamerasData, CamerasDetailedData, Complex } from "@/lib/types"
import { $host } from "./http"
import { AxiosResponse } from "axios"


export const getGroups = async () => {
    const resp: AxiosResponse = await $host.get('/groups/')
    return [...resp.data]
} 

export const createGroup = async (name: string) => {
    const resp: AxiosResponse = await $host.post('/groups', {"name": name})
    console.log('resp.data', resp.data)
    return resp.data
} 

export const deleteGroup = async (listId: string) => {
    const resp: AxiosResponse = await $host.delete(`/groups/${listId}`)
    return resp
} 

/////////////////////////////////////////////////////////

export const getCameras = async () => {
    const resp: AxiosResponse = await $host.get('/cameras')
    return resp.data
} 

export const createCamera = async (camera: CamerasData, complexId: string) => {
    const resp: AxiosResponse = await $host.post('/cameras', {
        url: camera.url,
        description: camera.description,
        id: camera.id,
        complex_uuid: camera.complex_uuid,
        active: camera.active
    })
    return resp.data
}

export const getDetailedCamera = async(uuid:string) => {
    const resp: AxiosResponse = await $host.get(`/cameras/${uuid}`)
    return resp.data
}

export const getDetailedComplex = async(uuid:string) => {
    const resp: AxiosResponse = await $host.get(`/complexes/${uuid}`)
    console.log('srdgdfg', uuid)
    return resp.data
}

export const createComplex = async (complex: Complex, listId: string) => {
    const resp: AxiosResponse = await $host.post('/complexes', {
        "name": complex.name,
        "ip": complex.ip,
        "port": complex.port,
        "login": complex.login,
        "password": complex.password,
        "group_uuid": listId,
    })
    return resp.data
} 

export const deleteComplex = async (uuid: string) => {
    const resp: AxiosResponse = await $host.delete(`/complexes/${uuid}`)
    return resp
} 

export const getComplexes = async() => {
    const resp: AxiosResponse = await $host.get('/complexes')
    return resp.data
} 

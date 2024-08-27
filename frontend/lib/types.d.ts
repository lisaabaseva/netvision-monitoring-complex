/**export type Complex = {
    uuid: number, 
    name?: string, 
    ip: string, 
    port: number, 
    status: string
}

export type ListItem = {
    listId: number,
    name: string,
    content?: Complex[]
}*/
export type ListType = {
    listId: string,
    name: string,
    status: {text: string, color: string},
    content: ComplexData[]
}

export type createList = {
    listId: string,
    name: string,
    status?: number,
    content: Complex[]
}

export type Complex = {
    name: string,
    uuid: string, 
    ip: string, 
    port: number,
    login?: string,
    password?: string,
    cameras?: CamerasData[]
    status?: {int: number, color: string, text: string},
    group_uuid?: string
}

export type GroupsData = {
    uuid: string,
    name: string
}

export type ComplexData = {
    name: string,
    uuid: string,
    ip: string,
    port: number,
    group_uuid?: string
}

export type CamerasData = {
    url: string,
    description: string,
    id: number,
    active: boolean,
    status?: number,
    complex_uuid: string
}

export type CamerasDetailedData = {
    uuid: string,
    ip: string,
    port: number,
    login: string,
    password: string,
    status?: number,
    group_uuid?: string
}
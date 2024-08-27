'use client'
import { getDetailedCamera, getDetailedComplex } from "@/http/someAPI"
import { CamerasData, CamerasDetailedData, Complex, createList, ListType } from "@/lib/types"
import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { Button, Form, Modal } from "react-bootstrap"
import CameraItem from "../CameraItem"
import AddCamera from "./AddCamera"

const ComplexInfo = ( props: {show: boolean, onHide: () => void, uuid: string, cameras?: CamerasData[]}) => {
  const [newComplex, setNewComplex] = useState<Complex>()
  let asd =     {description: 'props.newList.content.length', 
    id: '',
    url: '',
    active: true,
    status: 0,
    complex_uuid: ''}
  let filler = []
  for (let i = 0; i<50; i++) {
    filler.push(asd)
  }
  const [addCameraModal, setAddCameraModal] = useState(false)
  useEffect(( ) => {
    const  fetch = async() => {
      return getDetailedComplex(props.uuid)
    }
    fetch().then((resp:Complex) => {setNewComplex({...resp, cameras: props.cameras}) 
    console.log('srgfdrgdfg',props.cameras)}
      )
      console.log('cmplx', newComplex)
  }, [])

  const onCancel = () =>{
    console.log('props.show', props.show)
    props.onHide()
  }

  return (
    <Modal
      size = "lg"
      show={props.show}
      onHide={props.onHide}
      centered
      data-bs-theme="dark"
      className="text-white"
      dialogClassName="modal-66w"
    >
        <Modal.Header closeButton>
          <Modal.Title>Информация о комплексе</Modal.Title>
        </Modal.Header>
        <Modal.Body>
            <div className="inline-block w-fit p-4 pb-0">
              <div className="w-fit">
                Наименование:<br />
                {newComplex?.name}
              </div>
              <div className="w-fit">
                UUID: <br />
                {newComplex?.uuid}
              </div>
            </div>
            <div className="inline-block w-fit self-end p-4 pb-0">
              <div className="w-fit">
                IP: <br />
                {newComplex?.ip}
              </div>
              <div className="w-fit">
                PORT: <br />
                {newComplex?.port}
              </div>
            </div>
          <div className="p-4 pt-3">
            Статус: <br />
            {newComplex?.status?.text}
          </div>
          <button className="bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end w-fit p-2 rounded-xl px-4 ml-2" onClick={() => {setAddCameraModal(true)}}>
            <img src="/icons/plus-light.svg" alt="list" width={30} className="inline"/>
            <p className="inline ml-2">Добавить камеру</p>
          </button>
          <table className="w-full text-center">
            <thead>
              <tr>
                <th className="w-1/3">
                  Description
                </th>
                <th className="w-1/4">
                  URL
                </th>
                <th className="w-1/4">
                  ID
                </th>
                <th className="w-1/6">
                  ACTIVE
                </th>
                <th>
                  STATUS
                </th>
              </tr>
            </thead>
            <tbody className="">
              {(newComplex?.cameras?.map((camera) => {
                return (
                  <CameraItem key={camera.id} camera={camera}/>
                )
              }))

              }
            </tbody>
          </table>
        </Modal.Body>
        
        <Modal.Footer>
          <Button variant="secondary" onClick={onCancel}>Закрыть</Button>
        </Modal.Footer>
    </Modal>
  )
}

export default ComplexInfo

//<AddCamera show={addCameraModal} onHide={() => {setAddCameraModal(false)}} />
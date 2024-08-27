'use client'
import { createCamera, getDetailedCamera } from "@/http/someAPI"
import { CamerasDetailedData, Complex, createList, ListType } from "@/lib/types"
import { Dispatch, SetStateAction, useEffect, useState } from "react"
import { Button, Form, Modal } from "react-bootstrap"

const CameraInfo = ( props: {show: boolean, onHide: () => void, uuid: string}) => {
  const [newCamera, setNewCamera] = useState<Complex>({
    uuid: '', 
    ip: '', 
    port: 0,
    login: '',
    password: '',
    status: 0
  })

  useEffect(( ) => {
    const  fetch = async() => {
      return getDetailedCamera(props.uuid)
    }
    fetch().then((resp:Complex) => setNewCamera(resp))
  }, [])

  const onCancel = () =>{
    console.log('props.show', props.show)
    props.onHide()
  }

  return (
    <Modal
      show={props.show}
      onHide={props.onHide}
      centered
      data-bs-theme="dark"
      className="text-white"
    >
        <Modal.Header closeButton>
          <Modal.Title>Информация о комплексе</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div>
            Наименование: <br />
            {newCamera.uuid}
          </div>
          <div>
            UUID: <br />
            {newCamera.uuid}
          </div>
          <div>
            IP: <br />
            {newCamera.ip}
          </div>
          <div>
            PORT: <br />
            {newCamera.port}
          </div>
          <div>
            Логин: <br />
            {newCamera.login}
          </div>
          <div>
            Пароль: <br />
            {newCamera.password}
          </div>
          <div>
            Статус: <br />
            {newCamera.status}
          </div>
        </Modal.Body>

        <Modal.Footer>
          <Button variant="secondary" onClick={onCancel}>Закрыть</Button>
        </Modal.Footer>
        
    </Modal>
  )
}

export default CameraInfo
import { createCamera } from "@/http/someAPI"
import { CamerasData, CamerasDetailedData, Complex, createList, ListType } from "@/lib/types"
import { Dispatch, SetStateAction, useState } from "react"
import { Button, Form, Modal } from "react-bootstrap"

const AddCamera = ( props: {show: boolean, onHide: () => void, newList: createList}) => {
  const [newCamera, setNewCamera] = useState<CamerasData>({
    url: '', 
    description: '',
    id: 0,
    active:false,
    complex_uuid: ''
  })

  const submitHandler = () => {
    console.log('camera ', newCamera)
    createCamera(newCamera, props.newList.listId)
    props.onHide()
    setNewCamera({
      url: '', 
      description: '',
      id: 0,
      active:false,
      complex_uuid: ''
    })
  }
  const onCancel = () =>{
    props.onHide()
    setNewCamera({
      url: '', 
      description: '',
      id: 0,
      active:false,
      complex_uuid: ''})
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
          <Modal.Title>Добавить комплекс</Modal.Title>
        </Modal.Header>

        <Modal.Body>
          <Form>
            <Form.Group>
            <Form.Group>
              <Form.Label className="mr-2">Описание : </Form.Label>
              <Form.Control type="text" onChange={(e) => setNewCamera({...newCamera, description: e.target.value})}/>
            </Form.Group>
              <Form.Label className="mr-2">URL : </Form.Label>
              <Form.Control type="text" onChange={(e) => setNewCamera({...newCamera, url:e.target.value})}/>
            </Form.Group>
            <Form.Group>
              <Form.Label htmlFor="uuid" className="mr-2">ID : </Form.Label>
              <Form.Control type="number" className="remove-arrow" onChange={(e) => setNewCamera({...newCamera, id:parseInt(e.target.value)})}/>
            </Form.Group>
            <Form.Group>
              <Form.Label className="mr-2">Active : </Form.Label>
              <Form.Control type="checkbox" onChange={(e) => setNewCamera({...newCamera, login:e.target.value})}/>
            </Form.Group>
          </Form>
        </Modal.Body>

        <Modal.Footer>
          <Button variant="secondary" onClick={onCancel}>Отмена</Button>
          <Button variant="primary" onClick={submitHandler}>Добавить</Button>
        </Modal.Footer>
        
    </Modal>
  )
}


export default AddCamera

/**
 *             <Form.Group>
              <Form.Label className="mr-2">Status : </Form.Label>
              <Form.Control type="number" className="remove-arrow" onChange={(e) => {setNewCamera({...newCamera, status:parseInt(e.target.value)})}}/>
            </Form.Group>
 */
/**
 * <Form.Group>
              <Form.Label className="mr-2">UUID : </Form.Label>
              <Form.Control type="text" name="uuid" onChange={(e) => setNewCamera({...newCamera, uuid:e.target.value})}/>
            </Form.Group>
 */
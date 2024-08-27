'use client'
import { useEffect, useState } from "react"
import { Button, Form, Modal } from "react-bootstrap"
import AddCamera from "./AddComplex"
import { Complex, createList, ListType } from "@/lib/types"
import { useDispatch, useSelector } from "react-redux"
import { RootState } from "@/state/store"
import { addList, setList } from "@/state/listStore/listSlice"
import { createSelector } from "@reduxjs/toolkit"
import { createComplex, createGroup } from "@/http/someAPI"
import { useFetchAll } from "@/hooks/useFetchAll"
import { useRouter } from "next/router"

const AddList = ( props: {show: boolean, onHide: () => void}) => {
  const [AddCameraModal, setAddCameraModal] = useState(false)
  //const selectL = (state: RootState) => state.list 
  const [newList, setNewList] = useState<createList>({listId: '', name: '', status: 0, content: []})
  //const list: ListType[] = Array.from(useSelector((state: RootState) => state.list.values()))
  const dispatch = useDispatch()
  //const selectList = createSelector([selectL], (list) => {
    //return Array.from(list)
  //})
  //const list = selectList(state)
  const submitHandler = async() => {

    //console.log('newList', newList)
    //dispatch(addList(newList))
    //console.log('list', list)
    await createGroup(newList.name).then(resp => {newList.content.map((complex) => {createComplex(complex, resp.uuid)})})
    location.reload()
    setNewList({listId: '', name: '', status: 0, content: []})
    //dispatch(setList(await useFetchAll()))
    props.onHide()
  }
  const onCancel = () =>{
    setNewList({listId: '', name: '', status: 0, content: []})
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
      <div>
        <Modal.Header closeButton>
          <Modal.Title>Добавить список</Modal.Title>
        </Modal.Header>

        <Modal.Body>
          <Form onSubmit={submitHandler}>
            <Form.Group>
              <Form.Label>Название списка : </Form.Label>
              <Form.Control type="text" value={newList?.name} onChange={(e) => setNewList({...newList, name:e.target.value})}/>
            </Form.Group>
          </Form>
          <div className="mt-2 w-full flex flex-col">
            <p>Список камер :</p>
            <table className="w-full">
              <thead className="text-center">
                <tr>
                <th className="w-1/3">Наименование</th>
                  <th className="w-1/3">IP</th>
                  <th className="w-1/3">PORT</th>
                  
                </tr>
              </thead>
            </table>
              <div>
                {(newList.content)
                  ? <table className="w-full">
                      <tbody>
                      {newList.content.map((camera) => {
                        return (
                          <tr key={camera.ip + ':' + camera.port} className="w-full text-center">
                            <td className="w-1/3">Complex name</td>
                            <td className="w-1/3">{camera.ip}</td>
                            <td className="w-1/3">{camera.port}</td>
                            
                          </tr>
                        )
                      })}
                      </tbody>
                    </table>
                  : <div></div>
                }
              </div>

            <button className="bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end w-fit p-2 rounded-xl px-4 mt-2 self-center" onClick={() => {setAddCameraModal(true)}}>
              <img src="/icons/plus-light.svg" alt="list" width={30} className="inline"/>
              <p className="inline ml-2">Добавить комплекс</p>
            </button>
            <AddCamera show={AddCameraModal} onHide={() => {setAddCameraModal(false)}} newList={newList} setNewList={setNewList}/>
          </div>
        </Modal.Body>

        <Modal.Footer>
          <Button variant="secondary" onClick={onCancel}>Отмена</Button>
          <Button variant="primary" type="submit" onClick={submitHandler}>Добавить</Button>
        </Modal.Footer>
      </div>
    </Modal>
  )
}

export default AddList

//<td className="w-1/3">{camera.status}</td>
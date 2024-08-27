'use client'
import { useState } from "react"
import AddList from "./modals/AddList"

const Header = () => {
  const [AddListModal, setAddListModal] = useState(false)
  return (
    <header className=" w-5/6 border-b-2 mx-auto mt-6 pb-5 text-white">
      <a href="/">
        <button className="bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end w-fit p-2 rounded-xl px-4">
          <img src="/icons/list-light-2.svg" alt="list" width={30} className="inline"/>
        </button>
      </a>
      <button className="bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end w-fit p-2 rounded-xl px-4 ml-2" onClick={() => {setAddListModal(true)}}>
        <img src="/icons/plus-light.svg" alt="list" width={30} className="inline"/>
        <p className="inline ml-2">Добавить список</p>
      </button>
      <AddList show={AddListModal} onHide={() => {setAddListModal(false)}}/>
    </header>
  )
}

export default Header

/**
 * <header className=" w-5/6 border-b-2 mx-auto mt-6 pb-5">
      <button className="bg-gradient-to-b from-netvision-gradient-start to-netvision-gradient-end w-fit p-2 rounded-xl px-5">
        <img src="/icons/list-light-2.svg" alt="list" width={30}/>
      </button>
    </header>
 */
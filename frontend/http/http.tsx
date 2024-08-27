import axios from "axios";
const BASE_URL = process.env.CENSUS_URL || 'http://localhost:8000/'


const $host = axios.create({
    baseURL: BASE_URL
})

export {
    $host
}
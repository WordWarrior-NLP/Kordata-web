// store.js
// An extremely simple external store
import { writable } from 'svelte/store'
export default writable(0)

export let previousLocation = writable('')

// store.js
// An extremely simple external store
import { writable } from 'svelte/store'
export default writable(0)

export let previousLocation = writable('')
export let newestMainTitle = writable('')
export let duration = writable(0);
export let sideActive = writable(true);
export let selectedNews = writable(0);


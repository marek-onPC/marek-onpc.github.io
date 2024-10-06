import { getTokenFromMemory } from '$lib/memory';
import { writable } from 'svelte/store';

let sessionTokenFromMemory = getTokenFromMemory();

export const sessionToken = writable<string>(sessionTokenFromMemory);

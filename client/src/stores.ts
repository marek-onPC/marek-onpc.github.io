import { getTokenFromMemory } from '$lib/memory';
import { writable, readable } from 'svelte/store';
import type { AuthToken } from './types';

let sessionTokenFromMemory = getTokenFromMemory();

export const sessionToken = writable<AuthToken>(sessionTokenFromMemory);

export const isSafari = readable<boolean>(navigator.vendor === 'Apple Computer, Inc.');

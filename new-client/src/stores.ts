import { getTokenFromMemory } from '$lib/memory';
import { writable } from 'svelte/store';
import type { AuthToken } from './types';

let sessionTokenFromMemory = getTokenFromMemory();

export const sessionToken = writable<AuthToken>(sessionTokenFromMemory);

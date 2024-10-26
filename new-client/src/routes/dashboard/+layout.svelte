<script lang="ts">
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import { sessionToken } from '../../stores';
  import { removeTokenInMemory } from '$lib/memory';

  const logoutHandler = () => {
    removeTokenInMemory();
    sessionToken.set('');
    goto('/');
  };

  onMount(() => {
    if (!$sessionToken) {
      goto('/login');
    }
  });
</script>

<nav>
  <a href="/dashboard/new-cs">new cheat sheet</a>
  <a href="/dashboard">all cheat sheets</a>
  <button on:click={logoutHandler}>logout</button>
</nav>
<slot />

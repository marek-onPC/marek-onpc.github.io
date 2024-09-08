<script lang="ts">
    import { goto } from "$app/navigation";
    import { getTokenFromMemory } from "$lib/memory";
    import { onMount } from "svelte";

onMount(() => {
  let currentToken = getTokenFromMemory();

  if (!currentToken) {
    goto("/login")
  }
})
</script>

<slot />

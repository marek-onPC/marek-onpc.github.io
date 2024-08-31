<script lang="ts">
  let username: string = '';
  let password: string = '';

  const loginHandler = () => {
    console.log('username: ' + username);
    console.log('password: ' + password);
  };
</script>

<div class="login">
  <form>
    <input name="username" placeholder="Username" class="login__input" bind:value={username} />
    <input
      name="password"
      placeholder="Password"
      type="password"
      class="login__input"
      bind:value={password}
    />
  </form>

  <button class="login__submit" on:click={loginHandler}>Login</button>
  <p>{username}</p>
</div>

<style lang="scss">
  .login {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    min-height: calc(100vh - 10px);
  }
</style>

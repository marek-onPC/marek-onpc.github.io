import { ReactElement, ReactNode, useContext, useEffect } from "react";
import { AuthContext } from "../utils/AuthContext";
import { useNavigate } from "react-router-dom";

type Props = {
  children: ReactNode;
}

const Authorization = ({ children }: Props): ReactElement => {
  const history = useNavigate();
  const jwtContext: string = useContext(AuthContext);

  // const getUserName = async (): Promise<void> => {
  //   try {
  //     const response = await fetchClientGet(
  //       "/authpath",
  //       token
  //     );

  //     console.log(response);
  //   }
  //   catch (error) {
  //     console.log(error);
  //   }
  // }

  useEffect(() => {
    if (!jwtContext) {
      history("/login");
    }
  }, [jwtContext, history]);
  return (
    <>
      {children}
    </>
  );
};

export default Authorization;

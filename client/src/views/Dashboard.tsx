import { ReactElement, useEffect, useContext } from "react";
import { fetchClientGet } from "../helpers/fetchClient";
import { AuthContext } from "../utils/AuthContext";

const Dashboard = (): ReactElement => {
  const token: string = useContext(AuthContext);

  const getUserName = async (): Promise<void> => {
    try {
      const response = await fetchClientGet(
        "/authpath",
        token
      );
      
      console.log(response);
    }
    catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    getUserName();
  });

  return (
    <div>
      Dashboard
    </div>
  );
};

export default Dashboard;

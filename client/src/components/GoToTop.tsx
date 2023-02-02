import { ReactElement } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAnglesUp } from "@fortawesome/free-solid-svg-icons";
import { Fab, Fade } from "@mui/material";

const GoToTop = ({ isVisible }: { isVisible: boolean }): ReactElement => {
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    })
  };

  return (
    <Fade
      in={isVisible}
      timeout={1000}
    >
      <Fab
        variant="extended"
        style={{
          position: "fixed",
          right: 35,
          bottom: 55,
        }}
        onClick={scrollToTop}
      >
        <FontAwesomeIcon icon={faAnglesUp} />
      </Fab>
    </Fade>
  )
}

export default GoToTop;
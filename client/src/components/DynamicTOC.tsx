import { faAnglesUp } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Box, Divider, Fab, List, ListItem, ListItemButton, SwipeableDrawer, Typography } from "@mui/material";
import { ReactElement, useEffect, useState } from "react";

const DynamicTOC = (): ReactElement => {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const [headings, setHeadings] = useState<HTMLCollection | null>(null);

  const goToHeading = (id: string | null): void => {
    if (id) {
      const headingById = document.getElementById(id);
      window.scrollTo({
        top: headingById?.offsetTop,
        behavior: "smooth"
      })
    }
  }

  useEffect(() => {
    const queriedHeadings = document.getElementsByTagName("h2");
    setHeadings(queriedHeadings);
  }, [setHeadings])

  return (
    <>
      <Fab
        variant="extended"
        style={{
          position: "fixed",
          right: 35,
          bottom: 155,
        }}
        onClick={() => { setIsOpen(!isOpen) }}
      >
        <FontAwesomeIcon icon={faAnglesUp} />
      </Fab>

      <SwipeableDrawer
        anchor="right"
        open={isOpen}
        onClose={() => { setIsOpen(false) }}
        onOpen={() => { setIsOpen(true) }}
      >
        <Box
          role="presentation"
          sx={{
            height: "auto",
            minHeight: "fit-content",
            display: "flex",
            flexDirection: "column",
            bgcolor: "secondary.main",
          }}
        >
          <List>
            <ListItem disablePadding>
              <ListItemButton onClick={() => { setIsOpen(false) }}>
                <Typography
                  component="p"
                  color="primary"
                  sx={{ margin: "15px" }}
                  fontWeight={800}
                >
                  Close
                </Typography>
              </ListItemButton>
            </ListItem>
            <Divider />
            {headings && headings.length > 0 ? <> {[...headings].map((heading, index) => {
              return (
                <ListItem key={index} disablePadding>
                  <ListItemButton onClick={() => { goToHeading(heading.getAttribute("id")) }}
                  >
                    <Typography
                      component="p"
                      color="primary"
                      sx={{ margin: "5px 7.5px 10px", fontSize: "14px", letterSpacing: "-1px" }}
                      fontWeight={400}
                    >
                      {heading.textContent}
                    </Typography>
                  </ListItemButton>
                </ListItem>
              )
            })} </> : null}
          </List>
        </Box>

      </SwipeableDrawer>
    </>
  )
}

export default DynamicTOC;

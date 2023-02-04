import { faCircleXmark, faTable } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Divider, Fab, List, ListItem, ListItemButton, SwipeableDrawer, Typography } from "@mui/material";
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
      });
      setIsOpen(false);
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
          bottom: 25,
        }}
        onClick={() => { setIsOpen(!isOpen) }}
      >
        <FontAwesomeIcon icon={faTable} />
      </Fab>
      <SwipeableDrawer
        anchor="right"
        open={isOpen}
        onClose={() => { setIsOpen(false) }}
        onOpen={() => { setIsOpen(true) }}
      >
        <List sx={{ height: "-webkit-fill-available", display: "inline-table", bgcolor: "primary.main" }}>
          <ListItem disablePadding>
            <ListItemButton onClick={() => { setIsOpen(false) }}>
              <Typography
                component="p"
                color="secondary"
                sx={{ margin: "auto" }}
                fontWeight={800}
              >
                <FontAwesomeIcon icon={faCircleXmark} />
              </Typography>
            </ListItemButton>
          </ListItem>
          <Divider />
          {headings && headings.length > 0 ? <> {[...headings].map((heading, index) => {
            return (
              <>
                <ListItem key={index} disablePadding>
                  <ListItemButton onClick={() => { goToHeading(heading.getAttribute("id")) }}
                  >
                    <Typography
                      component="p"
                      color="secondary"
                      sx={{ margin: "5px 7.5px 10px 15px", fontSize: "14px", letterSpacing: "-1px" }}
                      fontWeight={700}
                    >
                      {heading.textContent}
                    </Typography>
                  </ListItemButton>
                </ListItem>
                <Divider />
              </>
            )
          })} </> : null}
        </List>
      </SwipeableDrawer>
    </>
  )
}

export default DynamicTOC;

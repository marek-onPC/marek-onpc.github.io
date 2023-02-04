import { ReactElement, useEffect, useState } from "react";

const DynamicTOC = (): ReactElement => {
  const [headings, setHeadings] = useState<HTMLCollection | null>(null);

  const goToHeading = (id: string | null) => {
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
      {headings && headings.length > 0 ? <> {[...headings].map((heading, index) => {
        return (
          <p
            key={index}
            onClick={() => { goToHeading(heading.getAttribute("id")) }}
          >
            {heading.textContent}
          </p>
        )
      })} </> : null}
    </>
  )
}

export default DynamicTOC;

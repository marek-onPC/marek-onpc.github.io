import { ReactElement, useEffect, useState, useRef, SetStateAction, Dispatch } from "react";
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import { Box, Button } from "@mui/material";

const modalStyle = {
  position: 'absolute' as 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: "auto",
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

const FaceVerification = (
  {
    showModal,
    setShowModal,
    setPhoto,
    isPhotoSet
  }: {
    showModal: boolean,
    setShowModal: Dispatch<SetStateAction<boolean>>,
    setPhoto: Dispatch<SetStateAction<null | string>>,
    isPhotoSet: boolean
  }): ReactElement => {
  const videoFrame = useRef<HTMLVideoElement>(null);
  const canvasFrame = useRef<HTMLCanvasElement>(null);
  const [capturedVideo, setCapturedVideo] = useState<MediaStream | null>(null);
  const [showCameraFrame, setShowCameraFrame] = useState<boolean>(true);

  const turnOnCamera = async () => {
    setShowCameraFrame(true)

    if (capturedVideo && videoFrame.current) {
      videoFrame.current.srcObject = capturedVideo
      videoFrame.current.play()
    }
  }

  const turnOffCamera = async () => {
    if (capturedVideo && videoFrame.current) {
      videoFrame.current.pause()
      videoFrame.current.srcObject = null

      capturedVideo.getTracks().forEach((track) => {
        track.stop();
      });
    }
    setShowModal(false)
  }

  const handlePhoto = () => {
    if (canvasFrame.current && videoFrame.current) {
      const context = canvasFrame.current.getContext("2d");

      if (context) {
        canvasFrame.current.width = videoFrame.current.videoWidth;
        canvasFrame.current.height = videoFrame.current.videoHeight;

        context.drawImage(videoFrame.current, 0, 0, videoFrame.current.videoWidth, videoFrame.current.videoHeight);
        setShowCameraFrame(false)
      }
    }
  }

  const usePhoto = () => {
    if (canvasFrame.current && videoFrame.current) {
      const data = canvasFrame.current.toDataURL("image/png");
      setPhoto(data)
    }
  }

  const getMediaStream = async (navigator: Navigator) => {
    if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
      const newMediaStream = await navigator.mediaDevices.getUserMedia({
        video: {
          width: {
            min: 480,
            ideal: 600,
            max: 768,
          },
          height: {
            min: 640,
            ideal: 800,
            max: 1024,
          },
        }
      })
      setCapturedVideo(newMediaStream)
    }
  }

  useEffect(() => {
    showModal && getMediaStream(navigator)
  }, [navigator, showModal])

  useEffect(() => {
    if (!isPhotoSet && showModal) {
      capturedVideo && setTimeout(turnOnCamera, 1000)
    } else {
      turnOffCamera();
    }
  }, [capturedVideo, isPhotoSet, showModal])


  return <Modal
    open={showModal}
    aria-labelledby="modal-modal-title"
    aria-describedby="modal-modal-description"
  >
    <Box sx={modalStyle}>
      <Typography id="modal-modal-title" variant="h6" component="h2" style={{ textAlign: "center" }}>
        Face verification
      </Typography>

      <video ref={videoFrame} style={{ display: showCameraFrame ? "block" : "none", height: 350 }}></video>
      <canvas style={{ display: showCameraFrame ? "none" : "block", height: 350 }} ref={canvasFrame}></canvas>

      {showCameraFrame ?
        <div style={{ display: "flex" }}>
          <Button
            sx={{
              width: 125,
              margin: "10px auto 0"
            }}
            onClick={handlePhoto}
            variant="contained"
          >
            Take photo
          </Button>
        </div>
        :
        <div style={{ display: "flex" }}>
          <Button
            sx={{
              width: 125,
              margin: "10px auto 0"
            }}
            onClick={usePhoto}
            variant="contained"
          >
            Use photo
          </Button>
          <Button
            sx={{
              width: 150,
              margin: "10px auto 0 10px"
            }}
            onClick={turnOnCamera}
            variant="contained"
          >
            Retake photo
          </Button>
        </div>}
    </Box>
  </Modal>
}

export default FaceVerification;
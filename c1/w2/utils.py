import tensorflow as tf

class callback(tf.keras.callbacks.Callback):
    def end_on_epoch(self, epoch, logs ={}):
        if (logs.get("Accuracy") >= 0.90):
            self.model.stop_training = True

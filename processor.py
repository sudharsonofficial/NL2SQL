from simplet5 import SimpleT5


class SpiderModel():
    def __init__(self) -> None:

        self.model = SimpleT5() #// Load the model here
        # self.model.from_pretrained(model_type="t5", model_name="t5-base")
        self.model.load_model("t5","spider_model_10epochs", use_gpu=False)


    def __preprocess(self): # add any parameters if required --> raw input string returns preprocessed input
        """
        Preprocess the text bofore fitting the model
        Add if required
        return the results
        """

    def __predict(self,text:str): # add the required parameters --> preprocessed input returns prediction

        """
        code to predict from self.model 
        return the results
        """
        pred = self.model.predict(text)

        return pred

    def __decode(self,pred:list) -> str : #add the required parameters --> Prediction result from the model returns final result
        """
        decode the result from the prediction
        """
        res = pred[0]
        return res

    def process(self, text:str) -> str:

        

        # pre_processed = self.__preprocess(text)

        prediction = self.__predict(text)

        result = self.__decode(prediction)

        return result



class CustomModel():
    def __init__(self) -> None:

        self.model = SimpleT5() #// Load the model here
        # self.model.from_pretrained(model_type="t5", model_name="t5-base")
        self.model.load_model("t5","CustomT5_CompleteData", use_gpu=False)

    def __preprocess(self): # add any parameters if required --> raw input string returns preprocessed input
        """
        Preprocess the text bofore fitting the model
        Add if required
        return the results
        """
        

    def __predict(self,text): # add the required parameters --> preprocessed input returns prediction

        """
        code to predict from self.model 
        return the results
        """
        pred = self.model.predict(text)

        return pred

    def __decode(self,pred:list) -> str : #add the required parameters --> Prediction result from the model returns final result
        """
        decode the result from the prediction
        """
        res = pred[0]
        return res

    def process(self, text:str) -> str:

        

        # pre_processed = self.__preprocess(text)

        prediction = self.__predict(text)

        result = self.__decode(prediction)

        return result